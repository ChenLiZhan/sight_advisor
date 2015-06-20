var map;
var markers = [];

$('.pull-down').each(function() {
    $(this).css('margin-top', $(this).parent().height() - $(this).height())
});

function initialize() {
    var mapProp = {
        center: new google.maps.LatLng(23.69781, 120.96051499999999),
        zoom: 5,
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
                    position: results[0].geometry.location
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


google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(function() {
    var keywordsSet = [];
    $('.keyword').click(function() {
        var keyword = $(this).data().keyword;
        $(this).toggleClass('clicked');
        if (keywordsSet.indexOf(keyword) > -1) {
            keywordsSet.splice(keywordsSet.indexOf(keyword), 1)
        } else {
            keywordsSet.push(keyword);
        }

        $.get("keyword.txt", function(data) {
            var sightsSet = [];
            clearOverlays();
            data = $.parseJSON(data);

            for (index in data) {
                for (keyw in keywordsSet) {
                    if (data[index]['keywords'].indexOf(keywordsSet[keyw]) > -1) {
                        sightsSet.push(data[index]['sight'])
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