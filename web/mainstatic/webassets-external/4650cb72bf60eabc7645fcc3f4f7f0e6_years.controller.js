function YearsCtrl($scope, $routeParams, Restangular, testFactory, items) {
    $scope.artist_id = $routeParams.artist_id
    getData($routeParams.artist_id);
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
	.module('teakwoodApp.components.years', [])

	.config(['$routeProvider', function($routeProvider) {
	  $routeProvider.when('/artist/:artist_id/years', {
	    templateUrl: 'components/years/years.html',
	    controller: 'YearsCtrl',
	    controllerAs: 'years'
	  });
	}])

	.controller('YearsCtrl', ['$scope', '$routeParams', 'Restangular', 'teakwoodApp.services.api', YearsCtrl]);