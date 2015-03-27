'use strict';


// Declare app level module which depends on filters, and services
angular.module('teakwoodApp', [
    'ngRoute',
    'restangular',
    'angularSoundManager',
    'teakwoodApp.controllers',
    // 'teakwoodApp.directives',
    // 'teakwoodApp.filters',
    'teakwoodApp.services'
  ]).
  config(['$routeProvider', function($routeProvider) {
      $routeProvider.when('/', { 
        controller: 'RootCtrl', 
        templateUrl: 'partials/artists.html'
      });
      $routeProvider.when('/list/:domain', {
        controller: 'ListCtrl', 
        templateUrl: 'partials/artist-view.html'
      });
      $routeProvider.when('/show/:domain', {
        controller: 'ShowCtrl', 
        templateUrl: 'partials/show.html'
      });
      $routeProvider.otherwise({redirectTo:'/'});
  }]).
  config(['RestangularProvider', function(RestangularProvider) {
    // point RestangularProvider.setBaseUrl to your API's URL_PREFIX
    RestangularProvider.setBaseUrl('http://192.168.1.4:8081');
    
    // RestangularProvider.setListTypeIsArray(false);
    RestangularProvider.setRestangularFields({
      id: "_id"
    });

    RestangularProvider.addResponseInterceptor(function (data, operation, what, url, response, deferred) {
    if (operation === 'getList') {
        // console.log(response);
        var newResponse = response.data._items;
        // newResponse.meta = response.data._meta;
        // newResponse.links = response.data._links;
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