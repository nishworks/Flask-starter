(function () {
  angular.module('MyApp')
  .filter('human_readable_date', function () {
    return function (standard_format_date) {
      return moment(standard_format_date).format('MMM D YYYY hh:mm a');
    }
  }).filter('unix_to_human_readable', function () {
    return function (unix_timestamp, timezone) {
      return moment(unix_timestamp).tz(timezone).format('MMM D YYYY HH:mm ');
    }
  })
}());