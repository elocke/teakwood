(function() {
  'use strict';

function ShowsController($scope, $stateParams, $state, $controller, Restangular, testFactory, items) {
    angular.extend(this, $controller('DefaultController', {$scope: $scope, $stateParams: $stateParams, $state: $state}));

    $scope.items = [];
    $scope.currentPage = 1;
    getData($stateParams.artist_id, $stateParams.year, $scope.currentPage);
    console.log($stateParams)
    console.log($state)
    console.log($scope)
    function getData(artistid, year, pagenum) {
      testFactory.getArtistShows(artistid, year, pagenum).then(function(items) {
          // console.log(items);
          $scope.totalItems = items.meta.total;
          angular.copy(items, $scope.items);              
        });      
    }

    $scope.pageChanged = function() {
      getData($routeParams.artist_id, $scope.currentPage);
    };
  };

angular
  .module('application.components.shows', [])
  .controller('ShowsController', ['$scope', '$stateParams', '$state', '$controller', 'Restangular', 'getApi', ShowsController]);


})();  