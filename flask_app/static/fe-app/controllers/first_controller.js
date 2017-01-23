(function () {
  angular.module('MyApp').controller('FirstController', function ($scope, $state, $stateParams, ApiService) {
    // Setup scope
    $scope.apiPath = 'example';
    $scope.$stateParams = $stateParams;
    $scope.$state = $state;
    $scope.apiDateFormat = ApiService.date_format;
    $scope.apiResultProcessors = {};
    $scope.apiCallIsInProgress = false;

    // Default Param values
    $scope.requiredParams = {
      from_time: moment().subtract(21, 'days').format($scope.apiDateFormat),
      to_time: moment().format($scope.apiDateFormat),
      timezone: moment.tz.guess()
    };
    // Supported Param values for some params. These are used to populate param_filter directives
    $scope.paramValues = {

    };

    //Initialize graph
    // API result processors path: function
    $scope.apiResultProcessors = {
      example: function(result){
        $scope.apiCallIsInProgress = False;
        // Do Whatever with result
      }

    };

    $scope.paramChangeCallback = function (name, value, api_url) {
      $stateParams[name] = value;
      $scope.apiCallIsInProgress = true;
      ApiService.query($scope.apiPath, $state, $stateParams, $scope.requiredParams, $scope.apiResultProcessors[api_url]);
    };

    $scope.multiParamChangeCallback = function (changes, api_url) {
      for (var param in changes) {
        $stateParams[param] = changes[param];
      }
      $scope.apiCallIsInProgress = true;
      ApiService.query($scope.apiPath, $state, $stateParams, $scope.requiredParams, $scope.apiResultProcessors[api_url]);
    };

    $scope.init = function () {
    };
    $scope.init();
  });
}());