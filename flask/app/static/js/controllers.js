/**
 * Created by Sandeep on 01/06/14.
 */
angular.module('teakwoodApp.controllers',[]).controller('TeakwoodListController',function($scope,$state,popupService,$window,Artist){

    $scope.artists=Artist.query();

    $scope.deleteShow=function(movie){
        if(popupService.showPopup('Really delete this?')){
            movie.$delete(function(){
                $window.location.href='';
            });
        }
    }

}).controller('TeakwoodViewController',function($scope,$stateParams,Artist){

    $scope.artist=Artist.get({id:$stateParams.id});

}).controller('TeakwoodCreateController',function($scope,$state,$stateParams,Artist){

    $scope.artist=new Artist();

    $scope.addArtist=function(){
        $scope.artist.$save(function(){
            $state.go('artists');
        });
    }

}).controller('TeakwoodEditController',function($scope,$state,$stateParams,Artist){

    $scope.updateArtist=function(){
        $scope.artist.$update(function(){
            $state.go('artists');
        });
    };

    $scope.loadArtist=function(){
        $scope.artist=Artist.get({id:$stateParams.id});
    };

    $scope.loadArtist();
});