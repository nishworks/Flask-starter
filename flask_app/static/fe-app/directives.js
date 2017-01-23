(function () {
  angular.module('MyApp').directive('dateRangeFilter', function () {
    return {
      restrict: 'AE',
      replace: true,
      scope: {
        paramChangeCallback: '&',
        dateFormat: '='
      },
      template: '<button type="button" class="btn btn-sm btn-success" value="">Time Range</button>',
      link: function (scope, element, attrs) {
        $(element).daterangepicker({
          'showDropdowns': false,
          'timePickerSeconds': true,
          'timePicker': true,
          'timePickerIncrement': 1,
          'startDate': moment().subtract(1, 'days').startOf('day'),
          'endDate': moment().add(5, 'days'),
          'minDate': '06/01/2015',
          'maxDate': moment().add(1, 'days').endOf('day'),
          'buttonClasses': 'btn btn-sm',
          'applyClass': 'btn-success',
          'cancelClass': 'btn-default',
          'autoApply': false,
          'ranges': {
            'Today': [
              moment().startOf('day'),
              moment().endOf('day')
            ],
            'Yesterday': [
              moment().subtract(1, 'day').startOf('day'),
              moment().subtract(1, 'day').endOf('day')
            ],
            'Last 7 Days': [
              moment().subtract(8, 'days').startOf('day'),
              moment().subtract(1, 'day').endOf('day')
            ],
            'Last 30 Days': [
              moment().subtract(31, 'days').startOf('day'),
              moment().subtract(1, 'day').endOf('day')
            ],
            'This Month': [
              moment().startOf('month'),
              moment().endOf('month')
            ],
            'Last Month': [
              moment().subtract(1, 'month').startOf('month'),
              moment().subtract(1, 'month').endOf('month')
            ]
          }
        }, function (start, end, label) {
            scope.paramChangeCallback({changes: {from_time: start.format(scope.dateFormat),to_time: end.format(scope.dateFormat)}});
        });
      }
    };
  }).directive('btnGroupParamFilter', function () {
    return {
      restrict: 'E',
      replace: true,
      scope: {
        paramName: '@',
        paramValues: '=',
        btnClass: '@',
        btnGroupClasses: '@',
        stateParams: '=',
        paramChangeCallback: '&'
      },
      templateUrl: 'static/fe-app/templates/directives/btn_group_param_filter.html',
      link: function (scope, element, attrs) {
      }
    };
  }).directive('dropDownParamFilter', function () {
    return {
      restrict: 'E',
      replace: true,
      scope: {
        paramName: '@',
        paramValues: '=',
        displayAllFilter: '@',
        btnClass: '@',
        stateParams: '=',
        paramChangeCallback: '&'
      },
      templateUrl: 'static/fe-app/templates/directives/drop_down_param_filter.html',
      link: function (scope, element, attrs) {
      }
    };
  });
}());