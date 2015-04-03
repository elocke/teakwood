'use strict';

/* Controllers */

angular.module('teakwoodApp.controllers', []).

  controller('RootCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
    $scope.items = [];
    $scope.currentPage = 1;
    getData();

    function getData() {
      var resource = Restangular.all('artists').getList({"where": "show_count>0", "sort": "-show_count", "page": $scope.currentPage}).then(function(items){
      // console.log(items)
      // $scope.items = items;
      // angular.forEach(items, function(item, key0){
          // console.log(item);
        // });
      $scope.totalItems = items.meta.total
      angular.copy(items, $scope.items)      
      });
    };
    // console.log($scope.totalItems)
    $scope.pageChanged = function() {
      getData();
    };

  }]).

  controller('ListCtrl', ['$scope', '$routeParams', 'Restangular', function ($scope, $routeParams, Restangular, items) {
    $scope.items = [];
    $scope.currentPage = 1;
    getData();

    function getData() {
      var resource = Restangular.service('shows', Restangular.one('artists', $routeParams.artist_id)).getList({"sort": "-date", "page": $scope.currentPage}).then(function(items){
      // $scope.items = items;
      // $scope.meta = items.meta;
      // console.log(items)
      // angular.forEach(items, function(item, key0){
        // $scope.date = item.date
        // $scope.location = item.location
        // $scope.id = item._id
        // });
      // console.log(items.meta)
      $scope.totalItems = items.meta.total
      angular.copy(items, $scope.items)
      });
    }
    // console.log($scope.totalItems)
    $scope.pageChanged = function() {
      getData();
    };
  }]).

  controller('ShowCtrl', ['$scope', '$routeParams', 'Restangular', function ($scope, $routeParams, Restangular, items) {
    var resource = Restangular.one('shows', $routeParams.show_id).get().then(function(show){
    $scope.show = show;
    // console.log(show.files)
    angular.forEach(show.files, function(file, key0){
      $scope.show.files[key0].url = 'http://archive.org/download/' + show.identifier + '/' + file.file_name;
      $scope.show.files[key0].artist = show.creator;
      $scope.show.files[key0].id = show.identifier + '-' + file.track;          
      });
    });
  }]);