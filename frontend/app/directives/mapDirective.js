(function(){
    angular.module('myapp').directive('mapDirective', mapDirective);

    function mapDirective() {
        var directive = {
            restrict: 'E',
            template: '<div id="map"></div>',
            controller: mapDirectiveCtrl,
            controllerAs: 'vm'
        };

        return directive;

    }

    function mapDirectiveCtrl ($http, mapService) {
        var vm = this;

        vm.displayMap = displayMap;
        displayMap();

        mapService.getData().then(function(resp){
            console.log(resp.data.burgerpoints[0].lang);
        });

        function displayMap() {
            google.maps.event.addDomListener(window, 'load');
        }

        function getCurrentPos () {
            navigator.geolocation.getCurrentPosition(showPosition);
        }
        getCurrentPos();

        function showPosition(position) {
            var lat = position.coords.latitude;
            var lon = position.coords.longitude;
            var myLatlng = new google.maps.LatLng(lat,lon);

            var mapOptions = {
              zoom: 14,
              center: myLatlng
            };
            var map = new google.maps.Map(document.getElementById("map"), mapOptions);

            var userPos = new google.maps.Marker({
                    position: new google.maps.LatLng(lat,lon)
            });
            userPos.setMap(map);


            $http.get('http://api.dajburgera.lucek.com.pl/get-burgers.json?lon='+lon+'&lat='+lat+'&limit=30')
                .then(successCallback);

            function successCallback(data) {
                console.log(data.data);
                for(i=1;i<data.data.data.length;i++) {
                    var a = new google.maps.Marker({
                        position: new google.maps.LatLng(data.data.data[i].lat,data.data.data[i].lon),
                        // title: data.data.data[i].name + " " + data.data.data[i].street
                    });
                    a.setMap(map);
                }
            }

        }



    }


})();
