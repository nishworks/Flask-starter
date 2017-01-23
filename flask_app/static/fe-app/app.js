(function () {
  angular
    .module('MyApp', ['ui.router', 'restangular', 'chart.js', 'ngSanitize', 'ngCsv', 'sticky'])
    .config(function ($interpolateProvider, RestangularProvider, $stateProvider, $urlRouterProvider) {
      $interpolateProvider.startSymbol('[[');
      $interpolateProvider.endSymbol(']]');
      var templateBaseUrl = 'static/fe-app/templates/';
      var apiUrl = 'api';
      RestangularProvider.setBaseUrl(apiUrl);
      var templateUrl = function (template_name) {
        return templateBaseUrl + template_name;
      };
      $urlRouterProvider.otherwise('/example');
      $stateProvider
        .state('example', {
          url: '/example?timezone&from_time',
          templateUrl: templateUrl('example.html'),
          controller: 'FirstController'
        })
        .state('example2', {
          url: '/example2?timezone&from_time',
          templateUrl: templateUrl('example2.html'),
          controller: 'SecondController'
        })
      ;
    });
}());