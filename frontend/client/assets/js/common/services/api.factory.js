(function() {
  'use strict';

function getApi(Restangular) {
  	console.log('factory');
  	var currentPage = 1;
	return {  
		getArtistList: function(pagenum) {
			return Restangular.all('artists').getList({"where": "show_count>0", "sort": "-show_count", "page": pagenum})
		},
		getArtistYears: function(artistid) {
			return Restangular.one('artists', artistid).get()
		},		
		getArtistShows: function(artistid, year, pagenum) {
			return Restangular.service('shows', Restangular.one('artists', artistid)).getList({"where": "year==" + year, "sort": "-date", "page": pagenum})
		},
		getShow: function(showid) {
			return Restangular.one('shows', showid).get()
		}
    }    
};

angular.module('application.services.api', [])
  .factory('getApi', ['Restangular', getApi]);


})();  