(function(){
	angular.module('myapp', []);

	angular.module('myapp').controller('mainCtrl', mainCtrl);

	function mainCtrl($scope, $timeout) {

		$scope.showBurger = false;

		$scope.giveMeBurger = function() {
			$timeout(function () {
				$scope.showBurger = true;
			}, 3000);
		};

	}

})();
