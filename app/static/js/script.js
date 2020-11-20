// (function worker() {
//   $.ajax({
//     url: '/',
//     success: function(data) {
//       $('.result').html(data);
//     },
//     complete: function() {
//       // Schedule the next request when the current one's complete
//       setTimeout(worker, 100000);
//     }
//   });
// })();
var socket = io();
// socket.on('connect', function() {
//   socket.emit('onConnect', {
//     data: 'I\'m connected!'
//   });
// });
socket.on('newData', function() {
  $.ajax({
    url: '/',
    success: function(data) {
      $('.result').html(data);
    },
  });
});
