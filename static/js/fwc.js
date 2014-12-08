(function ($, window, document, undefined) {

  // Get option values from feeds_subcat view.
  $("select#id_topregion").change(function(){
    // Tells if we make it inside change function.
    console.log('Inside $("select#id_topregion").change(function().');
    $.getJSON("/pages/feeds/places/"+$(this).val()+"/", function(j) {
      // Json objects.
      console.log(j);
      // Json objects count.
      console.log(j.length);
      var items = [];
      var options = '<option value="">Select place</option>';
      // $.each(j, function(j.fields['region'], j.fields['name'])) {
      //   items.push('<option value="' + j.fields['region'] + '">' + j.fields['name'] + '</options>');
      // }
      // $.each( data, function( key, val ) {
      //   items.push( "<li id='" + key + "'>" + val + "</li>" );
      // });

      // $( "<ul/>", {
      //   "class": "my-new-list",
      //   html: items.join( "" )
      // }).appendTo( "body" );
      for (var i = 0; i < j.length; i++) {
        // console.log(j.fields.name);
        options += '<option value="primary key goes here">place name here</option>';
        // options += '<option value="' + j.pk + '">' + j.fields['name'] + '</option>';
      }
      $("#id_subplace").html(options);
      $("#id_subplace option:first").attr('selected', 'selected');
      $("#id_subplace").attr('disabled', false);
    });
    $("#id_topregion").attr('selected', 'selected');
  });

  $('#id_place_0').attr('placeholder', 'Select a place');
  $('#id_building_0').attr('placeholder', 'Select a building');

  $('#id_region').on('change', function() {
    $('#id_place_0 option:eq(0)').prop("selected", true);
    $('#id_place_0').val('');
    $('#id_place_0').attr('placeholder', 'Select a place');
    $('#id_building_0 option:eq(0)').prop("selected", true);
    $('#id_building_0').val('');
    $('#id_building_0').attr('placeholder', 'Select a building');

    function newParameters(query) {
      query.region = $('#id_region').val();
    }

    $('#id_place_0').djselectable('option', 'prepareQuery', newParameters);
  });

  // $( "#id_place_0" ).blur(function() {
  //   console.log('CLICKED');
  //   console.log($('#id_place_0').val());

  //   function newParameters(query) {
  //     query.place = $('#id_place_0').val();
  //   }

  //   $('#id_building_0').djselectable('option', 'prepareQuery', newParameters);
  // });

  // $('#building-select a').on('click', function() {

  // });

})(jQuery, this, this.document);
