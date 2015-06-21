var map;
var markers = [];
var keywordsSet = [];
var markers_info = [];

function initialize() {
    var mapProp = {
        center: new google.maps.LatLng(23.69781, 120.96051499999999),
        zoom: 7,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

function addressMarker(sights, addresses) {
    for (var i = 0; i < sights.length; ++i) {
        geocoding(sights[i], addresses[i])
    }
}

function geocoding(sight, address) {
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({
        'address': address
    }, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            var infoWindow = new google.maps.InfoWindow(); // 設定氣泡框 (message bubble)，顯示地標相關的資訊
            markers_info.push(results[0].formatted_address);
            var html = "<h3>" + sight + "</h3>" + "<p> 地址: " + address + "</p>";
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location,
                animation: google.maps.Animation.BOUNCE
            });
            bindInfoWindow(marker, map, infoWindow, html); // 把對話框內容綁到地圖標記上頭
            markers.push(marker);
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}

function clearOverlays() {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
    markers.length = 0;
}

function changeKeywordsStyle() {

    // TODO: 選了一個將沒有的 keyword disabled 掉
    // $.get("keyword.txt", function(data) {
    //     for (index in data) {
    //         var found = false;
    //         for (i in keywordsSet) {
    //             if (data[index]['keywords'].indexOf(keywordsSet[i]) > -1) {
    //                 found = true;
    //                 break;
    //             }
    //         }
    //     }
    // });
    // $.get("keyword.txt", function(data) {
    //     data = $.parseJSON(data);

    //     for (index in data) {
    //         a = $.map(keywordsSet, function(value) {
    //             console.log(value);
    //             if (data[index]['keywords'].indexOf(value) > -1) {
    //                 return true;
    //             } else {
    //                 return false;
    //             }
    //         });
    //         if (a.indexOf(false) > -1) {
    //             $("a.keyword").each(function() {
    //                 if (data[index]['keywords'].indexOf($(this).data().keyword) > -1) {
    //                     $(this).toggleClass('disabled');
    //                 }
    //                 // console.log('a.key: ' + $(this).data().keyword);
    //                 // console.log(data[index]['keywords'][key]);
    //             });
    //         }
    //     }
    // for (index in data) {
    //     if (data[index]['keywords'].indexOf(value) > -1) {
    //         $("a.keyword").each(function() {
    //             if (data[index]['keywords'].indexOf($(this).data().keyword) == -1) {
    //                 $(this).toggleClass('disabled');
    //             }
    //             // console.log('a.key: ' + $(this).data().keyword);
    //             // console.log(data[index]['keywords'][key]);
    //         });
    //     }
    // }

    // });
}

// 設定地圖標記 (marker) 點開後的對話氣泡框 (message bubble)
function bindInfoWindow(marker, map, infoWindow, html) {
    // 除了 click 事件，也可以用 mouseover 等事件觸發氣泡框顯示
    google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(function() {
    $('.keyword').click(function() {
        var keyword = $(this).data().keyword;
        $(this).toggleClass('clicked');


        if (keywordsSet.indexOf(keyword) > -1) {
            keywordsSet.splice(keywordsSet.indexOf(keyword), 1)
        } else {
            keywordsSet.push(keyword);
        }

        // changeKeywordsStyle();

        $.get("keyword2.txt", function(data) {
            var sightsSet = [];
            var addressSet = [];
            clearOverlays();
            data = $.parseJSON(data);


            for (index in data) {
                for (keyw in keywordsSet) {
                    if (data[index]['keywords'].indexOf(keywordsSet[keyw]) > -1) {
                        sightsSet.push(data[index]['sight']);
                        addressSet.push(data[index]['address']);
                    }
                }
            }

            if (sightsSet.length > 0) {
                $.unique(sightsSet);
                $.unique(addressSet);
                addressMarker(sightsSet, addressSet);
            }
        });
    });
});