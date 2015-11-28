(function(){
    angular.module('myapp').factory('mapService', mapService);

    function mapService() {
        return {
            mapService: function() {
                function initialize() {
                    var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
                    var mapOptions = {
                      zoom: 4,
                      center: myLatlng
                    };
                    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

                    var marker = new google.maps.Marker({
                        position: new google.maps.LatLng(-39.363882,131.044922),
                        title:"Hello World!",
                        icon: 'http://icons.iconarchive.com/icons/position-relative/social-1/128/google-icon.png'
                    });

                    var markerTwo = new google.maps.Marker({
                        position: new google.maps.LatLng(-24.363882,131.044922),
                        title:"Hello World!"
                    });

                    // To add the marker to the map, call setMap();
                    marker.setMap(map);
                    markerTwo.setMap(map);
                }
                google.maps.event.addDomListener(window, 'load', initialize);
                initialize();
            }
       };
    }

    return mapService;

})();
