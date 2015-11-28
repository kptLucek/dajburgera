(function(){
    angular.module('myapp').factory('mapService', mapService);

    function mapService($http) {
        return  {
            getData: getData
        };

        function getData() {
            return $http.get('data.json')
                .then(successCallback);
            }
        function successCallback(data) {
            return data;
        }
    }


})();
