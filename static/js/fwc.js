(function ($, window, document, undefined) {
  // alert('test');
  console.log('TESTING');

  $(document).ready(function() {
      function newParameters(query) {
          query.state = $('#id_region').val();
      }
      $('#id_place_0').djselectable('option', 'prepareQuery', newParameters);
  });

})(jQuery, this, this.document);
