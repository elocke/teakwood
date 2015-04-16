'use strict';


// Declare app level module which depends on filters, and services
angular.module('teakwoodApp', [
    'ngRoute',
    'restangular',
    'angularSoundManager',
    'ui.bootstrap',
    'angular.filter',
    'teakwoodApp.services',
    'teakwoodApp.controllers',
    'teakwoodApp.directives',
    'teakwoodApp.filters'
  ]).
  config(['$routeProvider', function($routeProvider) {
      // console.log('hi')
      $routeProvider.when('/', { 
        controller: 'RootCtrl', 
        templateUrl: 'partials/artists.html'
      });
      $routeProvider.when('/artist/:artist_id/years/:year', {
        controller: 'ListCtrl', 
        templateUrl: 'partials/artist-view.html'
      });
      $routeProvider.when('/artist/:artist_id/years', {
        controller: 'YearCtrl', 
        templateUrl: 'partials/artist-years.html'
      });      
      $routeProvider.when('/show/:show_id', {
        controller: 'ShowCtrl', 
        templateUrl: 'partials/show.html'
      });
      $routeProvider.otherwise({redirectTo:'/'});
  }]).
  config(['RestangularProvider', function(RestangularProvider) {
    RestangularProvider.setBaseUrl('http://192.168.1.4:8080/api');
    RestangularProvider.setRestangularFields({
      id: "_id"
    });

    RestangularProvider.addResponseInterceptor(function (data, operation, what, url, response, deferred) {
    if (operation === 'getList') {
        // console.log(response);
        var newResponse = response.data._items;
        newResponse.meta = response.data._meta;
        newResponse.links = response.data._links;
        // console.log(newResponse);
        // newResponse.paging = response.paging;
        // newResponse.error = response.error;
        return newResponse;
    }
    if (operation === 'get') {
        // console.log(response);
        var newResponse = response.data;
        // newResponse.meta = response.data._meta;
        // newResponse.links = response.data._links;
        // console.log(newResponse);
        // newResponse.paging = response.paging;
        // newResponse.error = response.error;
        return newResponse;
    }    
    return response;
});      
  }]);