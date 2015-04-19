function ShowsCtrl($scope, $routeParams, Restangular, testFactory, items) {
    $scope.items = [];
    $scope.currentPage = 1;
    getData($routeParams.artist_id, $routeParams.year, $scope.currentPage);

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
	.module('teakwoodApp.components.shows', [])

	.config(['$routeProvider', function($routeProvider) {
	  $routeProvider.when('/artist/:artist_id/years/:year', {
	    templateUrl: 'components/shows/shows.html',
	    controller: 'ShowsCtrl',
	    controllerAs: 'shows'
	  });
	}])

	.controller('ShowsCtrl', ['$scope', '$routeParams', 'Restangular', 'teakwoodApp.services.api', ShowsCtrl]);