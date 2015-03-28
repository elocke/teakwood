'use strict';

/* Controllers */

angular.module('teakwoodApp.controllers', []).

  controller('RootCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
    // $scope.domains = Restangular.all("/").getList().$object;
    var resource = Restangular.all('artists').getList().then(function(items){
    // console.log(items)
    $scope.items = items;
    angular.forEach(items, function(item, key0){
        console.log(item);
      });
    });
  }]).

  controller('ListCtrl', ['$scope', '$routeParams', 'Restangular', function ($scope, $routeParams, Restangular, items) {
    var resource = Restangular.service('shows', Restangular.one('artists', $routeParams.artist_id)).getList().then(function(items){
    $scope.items = items;
    console.log(items)
    angular.forEach(items, function(item, key0){
      $scope.date = item.date
      $scope.location = item.location
      $scope.id = item._id
      });
    });
  }]).

  controller('ShowCtrl', ['$scope', '$routeParams', 'Restangular', function ($scope, $routeParams, Restangular, items) {
    var resource = Restangular.one('shows', $routeParams.show_id).get().then(function(show){
    $scope.show = show;
    console.log(show.files)
    angular.forEach(show.files, function(file, key0){
      $scope.show.files[key0].url = 'http://archive.org/download/' + show.identifier + '/' + file.file_name;
      $scope.show.files[key0].artist = show.creator;
      $scope.show.files[key0].id = show.identifier + '-' + file.track;          
      });
    });
  }]);