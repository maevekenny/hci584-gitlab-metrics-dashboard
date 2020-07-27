var transparent = true;
var transparentDemo = true;
var fixedTop = false;

var navbar_initialized = false;
var backgroundOrange = false;
var sidebar_mini_active = false;
var toggle_initialized = false;

var $html = $("html");
var $body = $("body");
var $navbar_minimize_fixed = $(".navbar-minimize-fixed");
var $collapse = $(".collapse");
var $navbar = $(".navbar");
var $tagsinput = $(".tagsinput");
var $selectpicker = $(".selectpicker");
var $navbar_color = $(".navbar[color-on-scroll]");
var $full_screen_map = $(".full-screen-map");
var $datetimepicker = $(".datetimepicker");
var $datepicker = $(".datepicker");
var $timepicker = $(".timepicker");

var seq = 0,
  delays = 80,
  durations = 500;
var seq2 = 0,
  delays2 = 80,
  durations2 = 500;

(function () {
  if ($(".main-panel").length != 0) {
    var ps = new PerfectScrollbar(".main-panel", {
      wheelSpeed: 2,
      wheelPropagation: true,
      minScrollbarLength: 20,
      suppressScrollX: true,
    });
  }

  if ($(".sidebar .sidebar-wrapper").length != 0) {
    var ps1 = new PerfectScrollbar(".sidebar .sidebar-wrapper");
    $(".table-responsive").each(function () {
      var ps2 = new PerfectScrollbar($(this)[0]);
    });
  }

  $html.addClass("perfect-scrollbar-on");
})();

$(document).ready(function () {
  var scroll_start = 0;
  var startchange = $(".row");
  var offset = startchange.offset();
  var scrollElement =
    navigator.platform.indexOf("Win") > -1 ? $(".ps") : $(window);
  scrollElement.scroll(function () {
    scroll_start = $(this).scrollTop();

    if (scroll_start > 50) {
      $(".navbar-minimize-fixed").css("opacity", "1");
    } else {
      $(".navbar-minimize-fixed").css("opacity", "0");
    }
  });

  $(document).scroll(function () {
    scroll_start = $(this).scrollTop();
    if (scroll_start > offset.top) {
      $(".navbar-minimize-fixed").css("opacity", "1");
    } else {
      $(".navbar-minimize-fixed").css("opacity", "0");
    }
  });

  if ($(".full-screen-map").length == 0 && $(".bd-docs").length == 0) {
    // On click navbar-collapse the menu will be white not transparent
    $(".collapse")
      .on("show.bs.collapse", function () {
        $(this)
          .closest(".navbar")
          .removeClass("navbar-transparent")
          .addClass("bg-white");
      })
      .on("hide.bs.collapse", function () {
        $(this)
          .closest(".navbar")
          .addClass("navbar-transparent")
          .removeClass("bg-white");
      });
  }

  blackDashboard.initMinimizeSidebar();

  $navbar = $(".navbar[color-on-scroll]");
  scroll_distance = $navbar.attr("color-on-scroll") || 500;
  if ($(".navbar[color-on-scroll]").length != 0) {
    blackDashboard.checkScrollForTransparentNavbar();
    $(window).on("scroll", blackDashboard.checkScrollForTransparentNavbar);
  }

  $(".form-control")
    .on("focus", function () {
      $(this).parent(".input-group").addClass("input-group-focus");
    })
    .on("blur", function () {
      $(this).parent(".input-group").removeClass("input-group-focus");
    });

  // Activate bootstrapSwitch
  $(".bootstrap-switch").each(function () {
    $this = $(this);
    data_on_label = $this.data("on-label") || "";
    data_off_label = $this.data("off-label") || "";

    $this.bootstrapSwitch({
      onText: data_on_label,
      offText: data_off_label,
    });
  });
});

$(window).resize(function () {
  // reset the seq for charts drawing animations
  seq = seq2 = 0;

  if ($full_screen_map.length == 0 && $(".bd-docs").length == 0) {
    var isExpanded = $navbar
      .find('[data-toggle="collapse"]')
      .attr("aria-expanded");
    if ($navbar.hasClass("bg-white") && $(window).width() > 991) {
      $navbar.removeClass("bg-white").addClass("navbar-transparent");
    } else if (
      $navbar.hasClass("navbar-transparent") &&
      $(window).width() < 991 &&
      isExpanded != "false"
    ) {
      $navbar.addClass("bg-white").removeClass("navbar-transparent");
    }
  }
});
