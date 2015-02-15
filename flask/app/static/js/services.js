angular.module('teakwoodApp.services',[]).factory('Artist',function($resource){
    return $resource('http://localhost:8081/artists/:id',{id:'@_id'},{
        update: {
            method: 'PUT'
        }
    });
}).service('popupService',function($window){
    this.showPopup=function(message){
        return $window.confirm(message);
    }
});