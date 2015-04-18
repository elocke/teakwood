function ArtistsCtrl($scope, Restangular, testFactory) {
    $scope.items = [];
    $scope.currentPage = 1;
    getData($scope.currentPage);

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
	.module('teakwoodApp.components.artists', [])

	.config(['$routeProvider', function($routeProvider) {
	  $routeProvider.when('/', {
	    templateUrl: 'frontend/static/app/components/artists/artists.html',
	    controller: 'ArtistsCtrl',
	    controllerAs: 'artists'
	  });
	}])

	.controller('ArtistsCtrl', ['$scope', 'Restangular', 'getApi', ArtistsCtrl]);