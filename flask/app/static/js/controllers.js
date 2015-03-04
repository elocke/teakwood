'use strict';

/* Controllers */

angular.module('teakwoodApp.controllers', []).

  controller('RootCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
    // $scope.domains = Restangular.all("/").getList().$object;
    var resource = Restangular.all("/").getList().then(function(items){
        $scope.items = items;
    });
  }]).

  controller('ListCtrl', ['$scope', 'Restangular', function ($scope, items) {
    // if (items._links.next != null) {
    //   $scope.nextpage = items._links.next.href.replace(items._links.parent.href,'');
    // }
    // if (items._links.prev != null) {
    //   $scope.prevpage = items._links.prev.href.replace(items._links.parent.href,'');
    // }
    // $scope.items = items;
    // $scope.domain = items.;

    $scope.shows = 'poop'
  }]);