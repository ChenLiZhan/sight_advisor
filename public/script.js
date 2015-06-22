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
    if (keywordsSet.length > 0) {
        $.get("keyword2.txt", function(data) {
            console.log(keywordsSet);
            data = $.parseJSON(data);
            final_key = []
            for (index in data) {
                var disabled = false;
                for (key in data[index]['keywords']) {
                    for (k in keywordsSet) {
                        if (data[index]['keywords'].indexOf(keywordsSet[k]) == -1) {
                            disabled = true;
                            break;
                        }
                    }
                    if (disabled) break;
                }


                if (!disabled) {
                    for (k in data[index]['keywords']) {
                        final_key.push(data[index]['keywords'][k]);
                        // $("a[data-keyword='" + data[index]['keywords'][k] + "']").addClass('disabled');
                    }
                }
            }

            var final_key_uniq = $.unique(final_key);
            $("a").each(function() {
                $(this).addClass('disabled');
            });
            for (i in final_key_uniq) {
                $("a[data-keyword='" + final_key_uniq[i] + "']").removeClass('disabled');
            }

        });
    } else {
        $("a").each(function() {
            $(this).removeClass('disabled');
        });

    }
}


// 設定地圖標記 (marker) 點開後的對話氣泡框 (message bubble)
function bindInfoWindow(marker, map, infoWindow, html) {
    // 除了 click 事件，也可以用 mouseover 等事件觸發氣泡框顯示
    google.maps.event.addListener(marker, 'mouseover', function() {
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
    });

    google.maps.event.addListener(marker, 'mouseout', function() {
        infoWindow.close()
    });
}

function arrayContainsAnotherArray(arry1, arry2) {
    var contained = false;
    for (var i = 0; i < arry2.length; i++) {
        if (arry1.indexOf(arry2[i]) > -1) {
            contained = true;
        } else {
            contained = false;
            break;
        }
    }
    return contained;
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

        changeKeywordsStyle();

        $.get("keyword2.txt", function(data) {
            var sightsSet = [];
            var addressSet = [];
            clearOverlays();
            data = $.parseJSON(data);


            for (index in data) {
                if (arrayContainsAnotherArray(data[index]['keywords'], keywordsSet)) {
                    sightsSet.push(data[index]['sight']);
                    addressSet.push(data[index]['address']);
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