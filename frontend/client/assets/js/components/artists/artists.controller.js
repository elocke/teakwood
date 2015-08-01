(function() {
  'use strict';

function ArtistsController($rootScope, $scope, $stateParams, $state, $controller, Restangular, testFactory) {
    angular.extend(this, $controller('DefaultController', {$scope: $scope, $stateParams: $stateParams, $state: $state}));
    console.log('artists load');
    console.log($state.get());
    $scope.items = [];
    $scope.currentPage = 1;
    getData($scope.currentPage);

    $scope.setYears = function(item) {
       $rootScope.years = item.years;   
       $rootScope.artist = item.name;
       $rootScope.artist_id = item._id;
      };

    function getData(pagenum) {
    testFactory.getArtistList(pagenum).then(function(items) {
        // console.log(items);
        $scope.totalItems = items.meta.total;
        angular.copy(items, $scope.items);              
      });
    };

    $scope.pageChanged = function() {
      getData($scope.currentPage);
    };

  };

angular
  .module('application.components.artists', [])
  .controller('ArtistsController', ['$rootScope', '$scope', '$stateParams', '$state', '$controller', 'Restangular', 'getApi', ArtistsController]);

})();  