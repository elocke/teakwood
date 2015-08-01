(function() {
  'use strict';

  angular.module('application', [
    'ui.router',
    'ngAnimate',

    //foundation
    'foundation',
    'foundation.dynamicRouting',
    'foundation.dynamicRouting.animations',

    //tealwppd requirements
    'restangular',
    'angularSoundManager',
    'infinite-scroll',
        
    //teakwoodApp
    'application.services.api',
    'application.common.audio-player',
    'application.components.artists',
    'application.components.years',
    'application.components.shows',
    'application.components.show'
  ])
    .config(config)
    .run(run)
  ;

  config.$inject = ['$urlRouterProvider', '$locationProvider', 'RestangularProvider'];

  function config($urlProvider, $locationProvider, RestangularProvider) {
    $urlProvider.otherwise('/');

    $locationProvider.html5Mode({
      enabled:false,
      requireBase: false 
    });

    $locationProvider.hashPrefix('!');

    RestangularProvider.setBaseUrl('http://localhost/api');
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

  }

  function run() {
    FastClick.attach(document.body);
  }

})();
