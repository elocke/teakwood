(function() {
  'use strict';

function YearsController($scope, $stateParams, $state, $controller, Restangular, testFactory, items) {
    angular.extend(this, $controller('DefaultController', {$scope: $scope, $stateParams: $stateParams, $state: $state}));

    // $scope.artist_id = $routeParams.artist_id
    console.log($stateParams)
    getData($stateParams.artist_id);
    function getData(artistid) {
      testFactory.getArtistYears(artistid).then(function(artist) {
        $scope.years = artist.years
        $scope.rights = artist.rights
        // angular.copy()
      });                
      console.log($scope);
    }
  };

angular
	.module('application.components.years', [])
	.controller('YearsController', ['$scope', '$stateParams', '$state', '$controller', 'Restangular', 'getApi', YearsController]);

})();  