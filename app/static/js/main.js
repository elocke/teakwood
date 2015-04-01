'use strict';
 
var app = angular.module('flaskApp',['ngRoute'])
    .controller('IndexController',[function(){
        var self = this;
        self.message = {};
        self.message.text = 'This is from angular!!!';
    }])
    .config(['$httpProvider','$routeProvider', '$locationProvider',
        function($httpProvider, $routeProvider, $locationProvider) {
        $routeProvider
        .when('/', {
            templateUrl: '/partials/landing.html',
            controller: 'IndexController',
            controllerAs:'ctrl'
        })
        .otherwise({
            redirectTo: '/'
        });
        $locationProvider.html5Mode(true);
    }]);



    