angular
	.module('teakwoodApp.core.audio-player')

	.directive('audioPlayer', function(){
		console.log('im being run');
		return {
		    restrict: 'AC',
		    templateUrl: 'frontend/static/app/components/core/audio-player/audio-player.html',
		    scope: true,
		    transclude : false,
		    controller: 'AudioCtrl'		
		}
	});