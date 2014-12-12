(function ($, window, document, undefined) {

  // Get option values from feeds_subcat view.
  $("select#id_region").change(function(){
    $.getJSON("/pages/feeds/places/"+$(this).val()+"/", function(j) {
      // Json objects.
      console.log(j);
      // Json objects count and data.
      console.log(j.length);
      console.log(j[0]['fields']);
      console.log(j[0]['fields']['name']);
      console.log(j[0]['pk']);

      var items = [];
      var options = '<option value="">Select place</option>';

      for (var i = 0; i < j.length; i++) {
        options += '<option value="' + j[i]['pk'] + '">' + j[i]['fields']['name'] + '</option>';
      }
      $("#id_place").html(options);
      $("#id_place option:first").attr('selected', 'selected');
      $("#id_place").attr('disabled', false);
    });
    $("#id_region").attr('selected', 'selected');
  });

  // Get option values from feeds_subcat view.
  $("select#id_place").change(function(){
    $.getJSON("/pages/feeds/buildings/"+$(this).val()+"/", function(j) {
      // Json objects.
      console.log(j);
      // Json objects count and data.
      console.log(j.length);
      console.log(j[0]['fields']);
      console.log(j[0]['fields']['name']);
      console.log(j[0]['pk']);

      var items = [];
      var options = '<option value="">Select place</option>';

      for (var i = 0; i < j.length; i++) {
        options += '<option value="' + j[i]['pk'] + '">' + j[i]['fields']['name'] + '</option>';
      }
      $("#id_building").html(options);
      $("#id_building option:first").attr('selected', 'selected');
      $("#id_building").attr('disabled', false);
    });
    $("#id_place").attr('selected', 'selected');
  });

  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  $("#roll-stats").click(function(){
    $('#id_strength').val(getRandomInt(6,19));
    $('#id_stamina').val(getRandomInt(6,19));
    $('#id_speed').val(getRandomInt(6,19));
    $('#id_agility').val(getRandomInt(6,19));
    $('#id_toughness').val(getRandomInt(6,19));
    $('#id_constitution').val(getRandomInt(6,19));
    $('#id_beauty').val(getRandomInt(6,19));
    $('#id_intelligence').val(getRandomInt(6,19));
    $('#id_logic').val(getRandomInt(6,19));
    $('#id_teaching').val(getRandomInt(6,19));
    $('#id_intuition').val(getRandomInt(6,19));
    $('#id_charisma').val(getRandomInt(6,19));
    $('#id_leadership').val(getRandomInt(6,19));
  });


  // Old selectable js, keeping for now.
  //
  // $('#id_place_0').attr('placeholder', 'Select a place');
  // $('#id_building_0').attr('placeholder', 'Select a building');

  // $('#id_region').on('change', function() {
  //   $('#id_place_0 option:eq(0)').prop("selected", true);
  //   $('#id_place_0').val('');
  //   $('#id_place_0').attr('placeholder', 'Select a place');
  //   $('#id_building_0 option:eq(0)').prop("selected", true);
  //   $('#id_building_0').val('');
  //   $('#id_building_0').attr('placeholder', 'Select a building');

  //   function newParameters(query) {
  //     query.region = $('#id_region').val();
  //   }

  //   $('#id_place_0').djselectable('option', 'prepareQuery', newParameters);
  // });

})(jQuery, this, this.document);
