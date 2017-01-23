(function () {
  angular.module('MyApp')
  .service('ApiService', function (Restangular) {
    this.date_format = 'YYYY-MM-DD HH:mm:ss';
    /*
     Fill required params which might be missing in stateParams
     */
    this.fillStateParamsWithMissingRequiredParameters = function ($stateParams, requiredParams) {
      var missingParam = false;
      for (var name in $stateParams) {
        if ($stateParams[name] == undefined && name in requiredParams) {
          missingParam = true;
          $stateParams[name] = requiredParams[name];
        }
      }
      return missingParam;
    };
    /*
     Call API without reloading state
     */
    this.query = function (apiPath, $state, $stateParams, requiredParams, resultProcessorCallback) {
      this.fillStateParamsWithMissingRequiredParameters($stateParams, requiredParams);
      $state.go($state.current, $stateParams, {notify: false});
      Restangular.one(apiPath).get($stateParams).then(function (result) {
        return resultProcessorCallback(result);
      });
    };
  });
}());