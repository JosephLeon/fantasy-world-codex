(function ($, window, document, undefined) {
  // alert('test');
  console.log('TESTING');

  console.log($('#id_region').val());
  function newParameters(query) {
      query.state = $('#id_region').val();
      console.log(query.state);
      console.log('Inside.');
  }
  $('#id_place_0').djselectable('option', 'prepareQuery', newParameters);

})(jQuery, this, this.document);
