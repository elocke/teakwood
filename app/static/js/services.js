'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('teakwoodApp.services', []).
  value('version', '0.1').

  factory('testFactory', ['Restangular', function (Restangular) {
  	console.log('factory');
  	var currentPage = 1;
	return {  
		getArtistList: function(pagenum) {
			return Restangular.all('artists').getList({"where": "show_count>0", "sort": "-show_count", "page": pagenum})
		},
		getArtistShows: function(artistid, pagenum) {
			return Restangular.service('shows', Restangular.one('artists', artistid)).getList({"sort": "-date", "page": pagenum})
		},
		getShow: function(showid) {
			return Restangular.one('shows', showid).get()
		}
    }    
}]);