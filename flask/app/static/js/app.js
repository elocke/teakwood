'use strict';


// Declare app level module which depends on filters, and services
angular.module('teakwoodApp', [
    'ngRoute',
    'restangular',
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
      $routeProvider.otherwise({redirectTo:'/'});
  }]).
  config(['RestangularProvider', function(RestangularProvider) {
    // point RestangularProvider.setBaseUrl to your API's URL_PREFIX
    RestangularProvider.setBaseUrl('http://192.168.1.4:8081/artists');
    
    // RestangularProvider.setListTypeIsArray(false);
    RestangularProvider.setRestangularFields({
      id: "_id"
    });

    RestangularProvider.addResponseInterceptor(function (data, operation, what, url, response, deferred) {
    if (operation === 'getList') {
        var newResponse = response.data._items;
        // newResponse.paging = response.paging;
        // newResponse.error = response.error;
        return newResponse;
    }
    return response;
});      
  }]);