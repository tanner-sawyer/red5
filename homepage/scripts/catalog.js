<script src="https://code.jquery.com/jquery.js"></script>
<script src="js/header.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/jquery.tablesorter(old).js"></script> 
<script src="js/jquery.tablesorter.widgets(old).js"></script>
<script type="text/javascript" src="js/moment.min.js"></script>
<script type="text/javascript" src="js/bootstrap-datetimepicker.js"></script>
<script>
var start = 0
var end = 0

var selectBetweenStartEnd = function (checked) {
  var rows = $("tr.workorder-clickable").filter(function () {
    return $(this).css("display") != "none" 
  })
  if (start > end){
    var temp = start
    start = end
    end = temp
  }
  for (var i = start; i < end; i++){
    //$(rows[i]).find('.tc-checkbox').trigger("click")
    if(!checked) {
      $(rows[i]).find('.tc-checkbox').find('.glyphicon').addClass("glyphicon-unchecked").removeClass("glyphicon-check")
      $(rows[i]).removeClass("selected")
    } else {
      $(rows[i]).find('.tc-checkbox').find('.glyphicon').removeClass("glyphicon-unchecked").addClass("glyphicon-check")
      $(rows[i]).addClass("selected")
    }
  }
}

$('tbody tr').on('click', function (evt) {

  var id = $(evt.target).parent().attr('id')
  var form = $('<form method="post" action="tc-doc_view-workorder.php" hidden></form>')
  var input = $('<input hidden name="id" value="'+id+'"></input>')
  form.append(input)
  $('body').append(form)
  form.submit()
  // var id = $(evt.target).parent().attr('id')
  // var name = $(evt.target).parent().attr('data-name')
  // var form = $('<form method="post" action="tc-doc_assignWorkorder.php" hidden></form>')
  // var input = $('<input hidden name="id" value="'+id+'"></input>')
  // $("#myModal").modal('show');
  // $(".modal-body").find("#wo-id").val(id);
  // $(".modal-body").find(".wo-name").html(name);

  // $('body').append(form)
  // form.submit()
  //window.location = 'tc-records_view-record.php'
})
$('tbody tr td:first-child input').on('click', function (evt) {
  evt.stopPropagation()
})

$('tbody tr td:first-child').on('click', function (evt) {
  evt.stopPropagation()
  $(evt.target).find(".btn").trigger("click")
})

$('.tc-checkbox > span').on("click", function (evt) {
  var shiftPressed = 0
  var event = evt || window.event
  shiftPressed = event.shiftKey
  if(!shiftPressed) {
    start = $(evt.target).toggleClass("glyphicon-unchecked glyphicon-check").closest("tr").toggleClass("selected").prevAll("tr").filter(function () {
      return $(this).css("display") != "none" 
    }).length
  } else {
    end = $(evt.target).toggleClass("glyphicon-unchecked glyphicon-check").closest("tr").toggleClass("selected").prevAll("tr").filter(function () {
      return $(this).css("display") != "none" 
    }).length
    var checked = $(evt.target).hasClass("glyphicon-check")
    selectBetweenStartEnd(checked)
  }
  evt.stopPropagation()
})

$('.tc-checkbox').on("click", function (evt) {
  $(evt.target).find('.glyphicon').toggleClass("glyphicon-unchecked glyphicon-check")
  var shiftPressed = 0
  var event = evt || window.event
  shiftPressed = event.shiftKey
  if(!shiftPressed) {
    start = $(evt.target).closest("tr").toggleClass("selected").prevAll("tr").filter(function () {
      return $(this).css("display") != "none" 
    }).length
  } else {
    end = $(evt.target).closest("tr").toggleClass("selected").prevAll("tr").filter(function () {
      return $(this).css("display") != "none" 
    }).length
    var checked = $(evt.target).find('.glyphicon').hasClass("glyphicon-check")
    selectBetweenStartEnd(checked)
  }
  evt.stopPropagation()
})

var workorderTextExtraction = function(node)  
{  
    // extract data from markup and return it  
    return node.innerHTML.split("-").join("").toLowerCase();
} 

$(function(){
  
  $.extend($.tablesorter.themes.bootstrap, {
    // these classes are added to the table. To see other table classes available,
    // look here: http://twitter.github.com/bootstrap/base-css.html#tables
    table      : 'table table-bordered',
    caption    : 'caption',
    header     : 'bootstrap-header', // give the header a gradient background
    footerRow  : '',
    footerCells: '',
    icons      : '', // add "icon-white" to make them white; this icon class is added to the <i> in the header
    sortNone   : 'bootstrap-icon-unsorted',
    sortAsc    : 'icon-chevron-up glyphicon glyphicon-chevron-up',     // includes classes for Bootstrap v2 & v3
    sortDesc   : 'icon-chevron-down glyphicon glyphicon-chevron-down', // includes classes for Bootstrap v2 & v3
    active     : '', // applied when column is sorted
    hover      : '', // use custom css here - bootstrap class may not override it
    filterRow  : '', // filter row class
    even       : '', // odd row zebra striping
    odd        : ''  // even row zebra striping
    });

  // hide child rows
  $('.tablesorter-childRow td').hide();
  
  $("#workOrderTable-Table").tablesorter({

    // hidden filter input/selects will resize the columns, so try to minimize the change
    widthFixed : true,

    // initialize zebra striping and filter widgets
    widgets: ["filter", "stickyHeaders", "zebra"],
  
  sortList: [[1,0]],

    // headers: { 5: { sorter: false, filter: false } },

    widgetOptions : {

      zebra: ["even", "odd"],

      stickyHeaders_offset: '50px',

      // css class applied to the table row containing the filters & the inputs within that row
      filter_cssFilter   : 'tablesorter-filter',

      // If there are child rows in the table (rows with class name from "cssChildRow" option)
      // and this option is true and a match is found anywhere in the child row, then it will make that row
      // visible; default is false
      filter_childRows   : false,

      // if true, filters are collapsed initially, but can be revealed by hovering over the grey bar immediately
      // below the header row. Additionally, tabbing through the document will open the filter row when an input gets focus
      filter_hideFilters : false,

      // Set this option to false to make the searches case sensitive
      filter_ignoreCase  : true,

      // jQuery selector string of an element used to reset the filters
      filter_reset : '.reset',

      // Delay in milliseconds before the filter widget starts searching; This option prevents searching for
      // every character while typing and should make searching large tables faster.
      filter_searchDelay : 300,

      // Set this option to true to use the filter to find text from the start of the column
      // So typing in "a" will find "albert" but not "frank", both have a's; default is false
      filter_startsWith  : false,
    
    dateFormat : "mmddyyyy",//set the default date format


      // Add select box to 4th column (zero-based index)
      // each option has an associated function that returns a boolean
      // function variables:
      // e = exact text from cell
      // n = normalized value returned by the column parser
      // f = search filter input value
      // i = column index
      filter_functions : {

        2 : function (e, n, f, i, $r) {
          n = n.split("-").join("").toLowerCase()
          f = f.split("-").join("").toLowerCase()
          if(n.search(f) >= 0) {
            return true
          } else {
            return false
          }
        },

        8 : {
          "active/on hold" : function (e, n, f, i, $r) {
            fArr = f.split("/")
            return fArr[0] === e || fArr[1] === e
          },
          "active" : function (e, n, f, i, $r) {
            return e === f
          },
          "canceled" : function (e, n, f, i, $r) {
            return e === f
          },
          "complete" : function (e, n, f, i, $r) {
            return e === f
          },
          "on hold" : function (e, n, f, i, $r) {
            return e === f
          }
        }
      }
    }
  });
});

var countTheLeak = 0
function updateTable () {
  countTheLeak++
  console.log(countTheLeak)
  $('input').parent().addClass('clearable')
  $('input').unbind('focus').on('focus', function (evt) {
    var dataColumn = $(evt.target).attr("data-column")
    $('input[data-column="'+dataColumn+'"]').trigger("search-click")
  }).unbind('search-click').on('search-click', function (evt){
    var that = $(evt.target)
    if(!$(evt.target).next('span').length){
      $('<span class="glyphicon glyphicon-remove search-clear">').insertAfter(that)
        .on('click', function (evt) {
          var dataColumn = that.attr("data-column")
          $('input[data-column="'+dataColumn+'"]').next().trigger("search-clear")
          that.val('')
          $(evt.target).remove()
        }).on('search-clear', function (evt) {
          $(evt.target).prev().val('').trigger('change')
          $(evt.target).remove()
        })
    }
  })
  $('input').unbind('blur').on('blur', function (evt) {
    var dataColumn = $(evt.target).attr("data-column")
    $('input[data-column="'+dataColumn+'"]').trigger("search-blur")
  }).unbind('search-blur').on('search-blur', function (evt){
    if(!$(evt.target).val()){
      $(evt.target).next().remove()
    }
  })

  $('input.disabled').addClass('hidden')

  $("thead.tablesorter-stickyHeader > tr.tablesorter-filter-row > td.clearable > input.tablesorter-filter").unbind('blur').on("blur", function (evt) {
    if (evt.target.value){
      var dataColumn = $(evt.target).attr("data-column")
      $("thead:not(.tablesorter-stickyHeader) > tr.tablesorter-filter-row > td.clearable > input.tablesorter-filter[data-column="+dataColumn+"]").focus()
    }
  })

  var datetimepickerOptions = { pickTime: false, showToday: true }
  $("thead").find("input[placeholder=Date]").datetimepicker(datetimepickerOptions)
  $("thead").find("input[placeholder=Date]").unbind('click').on('click', function () {
    $(this).trigger("focus")
  })
  $("#workOrderTable-Table-sticky").find("input[placeholder=Date]").on("blur", function (evt) {
    $("#workOrderTable-Table").find("input[placeholder=Date]").blur()
  })

  $("input[data-column=2]").trigger("focus")

  $(".completeBtn").unbind('click').on("click", function (evt) {
    var workorders = []
    $.each($(".selectableOrder > .glyphicon-check"), function (index, value) {
      workorders.push($(value).closest("tr").attr("id"))
    })
    if (workorders.length){
      $.post("tc-doc_markComplete.php", { 'workorders[]': workorders}, function (data) {
       location.reload();
      })
    } else {
      $(".closemultipleAlert").fadeIn()
      setTimeout(function () {
        $(".closemultipleAlert").fadeOut()
      }, 5000)
    }
  })


  $(".printBtn").unbind('click').on("click", function (evt) {
    var printTBody = $("#printTBody").html("")
    var workorders = []
    $.each($(".selectableOrder > .glyphicon-check"), function (index, value) {
      var tr = $(value).closest("tr")
      workorders.push(tr.attr("id"))
      var trPrint = $("<tr></tr>")
      trPrint.attr('class', tr.attr('class')) 
      trPrint.append(tr.find(".printable").clone()) 
      printTBody.append(trPrint)
    })
    if (workorders.length){
      window.print()
    } else {
      $(".printmultipleAlert").fadeIn()
      setTimeout(function () {
        $(".printmultipleAlert").fadeOut()
      }, 5000)
    }
  })

    
}

$(window).load(function () {
  updateTable()
})
</script>