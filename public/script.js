var map;
var markers = [];
var keywordsSet = [];

function initialize() {
    var mapProp = {
        center: new google.maps.LatLng(23.69781, 120.96051499999999),
        zoom: 7,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

    // var myCenter = new google.maps.LatLng(51.508742, -0.120850);
    // var marker = new google.maps.Marker({
    //     position: myCenter,
    // });

    // marker.setMap(map);
}

function addressMarker(addresses) {
    for (add in addresses) {
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode({
            'address': addresses[add]
        }, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location,
                    animation: google.maps.Animation.BOUNCE
                });
                markers.push(marker);
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });

    }
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

        console.log(keywordsSet);
        // changeKeywordsStyle();

        $.get("keyword2.txt", function(data) {
            var sightsSet = [];
            clearOverlays();
            data = $.parseJSON(data);

            console.log(data);

            for (index in data) {
                for (keyw in keywordsSet) {
                    if (data[index]['keywords'].indexOf(keywordsSet[keyw]) > -1) {
                        sightsSet.push(data[index]['sight']);
                    }
                }
            }

            if (sightsSet.length > 0) {
                $.unique(sightsSet);
                addressMarker(sightsSet);
            }
        });
    });
});