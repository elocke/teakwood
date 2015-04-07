'use strict';

/* Controllers */

angular.module('teakwoodApp.controllers', []).

  controller('RootCtrl', ['$scope', 'Restangular', 'testFactory', function ($scope, Restangular, testFactory) {
    $scope.items = [];
    $scope.currentPage = 1;
    getData($scope.currentPage);

    function getData(pagenum) {
    testFactory.getArtistList(pagenum).then(function(items) {
        // console.log(items);
        $scope.totalItems = items.meta.total;
        angular.copy(items, $scope.items);              
      });
    };

    $scope.pageChanged = function() {
      getData($scope.currentPage);
    };

  }]).

  controller('ListCtrl', ['$scope', '$routeParams', 'Restangular', 'testFactory', function ($scope, $routeParams, Restangular, testFactory, items) {
    $scope.items = [];
    $scope.currentPage = 1;
    getData($routeParams.artist_id, $scope.currentPage);

    function getData(artistid, pagenum) {
      testFactory.getArtistShows(artistid, pagenum).then(function(items) {
          // console.log(items);
          $scope.totalItems = items.meta.total;
          angular.copy(items, $scope.items);              
        });      
    }

    $scope.pageChanged = function() {
      getData($routeParams.artist_id, $scope.currentPage);
    };
  }]).

  controller('ShowCtrl', ['$scope', '$routeParams', 'Restangular', 'testFactory', function ($scope, $routeParams, Restangular, testFactory, items) {
    getData($routeParams.show_id);
    function getData(showid) {
      testFactory.getShow(showid).then(function(show) {
        angular.forEach(show.files, function(file, key0){
          show.files[key0].url = 'http://archive.org/download/' + show.identifier + '/' + file.file_name;
          show.files[key0].artist = show.creator;
          show.files[key0].id = show.identifier + '-' + file.track;          
          });
        $scope.show = show        
      });                
      console.log($scope);
    }
  }]);