'use strict';

/* Controllers */

angular.module('teakwoodApp.controllers', []).

  controller('RootCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
    // $scope.domains = Restangular.all("/").getList().$object;
    var resource = Restangular.all('artists').getList().then(function(items){
    // console.log(items)
    $scope.items = items;
    angular.forEach(items, function(item, key0){
        // console.log(items);
      });
    });
  }]).

  controller('ListCtrl', ['$scope', 'Restangular', function ($scope, Restangular, items) {
    var resource = Restangular.service('shows', Restangular.one('artists', '5514f9f3cf730500128502e5')).getList().then(function(items){
    $scope.items = items;
    console.log(items)
    angular.forEach(items, function(item, key0){
      $scope.date = item.date
      $scope.location = item.location
      $scope.id = item._id
      });
    });
  }]).

  controller('ShowCtrl', ['$scope', 'Restangular', function ($scope, Restangular, items) {
    var resource = Restangular.one('shows', '55150b38b9c8f40013219e03').get().then(function(show){
    $scope.show = show;
    console.log(show.files)
    angular.forEach(show.files, function(file, key0){
      $scope.show.files[key0].url = 'http://archive.org/download/' + show.identifier + '/' + file.file_name;
      $scope.show.files[key0].artist = show.creator;
      $scope.show.files[key0].id = show.identifier + '-' + file.track;          
      });
    });
  }]);