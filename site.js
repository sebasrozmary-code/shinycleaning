/* Shiny Cleaning — gedeeld script voor alle pagina's.
   - mobiel menu en submenu's
   - offerteformulier verstuurt via WhatsApp (of e-mail), geen server nodig
   - jaartal in de footer
   Werkt zonder frameworks; de site blijft bruikbaar zonder JavaScript. */
(function () {
  "use strict";

  var WA = "32466307915";
  var MAIL = "info@shinycleaning.be";
  var lang = (document.documentElement.lang || "nl").slice(0, 2);

  var T = {
    nl: {
      hi: "Hallo Shiny Cleaning! Ik wil graag een prijs.",
      type: "Klant", services: "Diensten", name: "Naam", company: "Bedrijf", email: "E-mail",
      phone: "Telefoon", town: "Gemeente", freq: "Frequentie", msg: "Omschrijving",
      photos: "Ik stuur hierna foto's van de klus.", subject: "Offerteaanvraag via de website",
      check: "Vul de verplichte velden in (met *)."
    },
    fr: {
      hi: "Bonjour Shiny Cleaning ! Je souhaite recevoir un prix.",
      type: "Client", services: "Services", name: "Nom", company: "Société", email: "E-mail",
      phone: "Téléphone", town: "Commune", freq: "Fréquence", msg: "Description",
      photos: "J'envoie ensuite des photos du chantier.", subject: "Demande de devis via le site",
      check: "Veuillez remplir les champs obligatoires (*)."
    },
    en: {
      hi: "Hello Shiny Cleaning! I would like a quote.",
      type: "Customer", services: "Services", name: "Name", company: "Company", email: "Email",
      phone: "Phone", town: "Municipality", freq: "Frequency", msg: "Description",
      photos: "I will send photos of the job next.", subject: "Quote request via the website",
      check: "Please fill in the required fields (*)."
    }
  }[lang] || null;

  /* ---------- menu ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
    nav.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (a && a.getAttribute("href").indexOf("#") !== -1) {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
      }
    });
  }
  document.querySelectorAll(".sub-toggle").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var li = btn.closest(".has-sub");
      var open = btn.getAttribute("aria-expanded") === "true";
      document.querySelectorAll(".has-sub.is-open").forEach(function (o) {
        if (o !== li) { o.classList.remove("is-open"); o.querySelector(".sub-toggle").setAttribute("aria-expanded", "false"); }
      });
      btn.setAttribute("aria-expanded", String(!open));
      li.classList.toggle("is-open", !open);
    });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      document.querySelectorAll(".has-sub.is-open").forEach(function (o) {
        o.classList.remove("is-open"); o.querySelector(".sub-toggle").setAttribute("aria-expanded", "false");
      });
    }
  });

  /* ---------- jaartal ---------- */
  var jaar = document.getElementById("jaar");
  if (jaar) jaar.textContent = new Date().getFullYear();

  /* klikken op bel- en WhatsApp-knoppen meten (werkt zodra er analytics op staat) */
  document.addEventListener("click", function (e) {
    var a = e.target.closest('a[href^="tel:"], a[href*="wa.me/"]');
    if (!a) return;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: a.href.indexOf("tel:") === 0 ? "klik_bellen" : "klik_whatsapp", pagina: location.pathname });
  });

  /* ---------- zwevende WhatsApp-knop: verborgen zolang er al een WhatsApp-knop in beeld is ---------- */
  var fl = document.querySelector(".float-wa");
  var waKnoppen = document.querySelectorAll(".btn-wa");
  if (fl && waKnoppen.length && "IntersectionObserver" in window) {
    var inBeeld = [];
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var i = inBeeld.indexOf(en.target);
        if (en.isIntersecting && i === -1) inBeeld.push(en.target);
        if (!en.isIntersecting && i !== -1) inBeeld.splice(i, 1);
      });
      fl.classList.toggle("is-hidden", inBeeld.length > 0);
    });
    fl.classList.add("is-hidden");
    Array.prototype.forEach.call(waKnoppen, function (el) { io.observe(el); });
  }

  /* ---------- offerteformulier: WhatsApp of e-mail ---------- */
  var form = document.getElementById("quote-form");
  if (!form || !T) return;

  function val(id) { var el = document.getElementById(id); return el ? el.value.trim() : ""; }
  function compose() {
    var type = form.querySelector('input[name="klanttype"]:checked');
    var labelOf = function (input) { var s = input.closest("label").querySelector("span"); return s ? s.textContent.trim() : input.value; };
    var diensten = Array.prototype.map.call(form.querySelectorAll('input[name="dienst[]"]:checked'), labelOf);
    var freq = document.getElementById("frequentie");
    var lines = [T.hi, ""];
    if (type) lines.push(T.type + ": " + labelOf(type));
    if (diensten.length) lines.push(T.services + ": " + diensten.join(", "));
    lines.push(T.name + ": " + val("naam"));
    if (val("bedrijf")) lines.push(T.company + ": " + val("bedrijf"));
    lines.push(T.town + ": " + val("gemeente"));
    lines.push(T.phone + ": " + val("telefoon"));
    if (val("email")) lines.push(T.email + ": " + val("email"));
    if (freq && freq.value) lines.push(T.freq + ": " + freq.options[freq.selectedIndex].text);
    if (val("bericht")) { lines.push(""); lines.push(T.msg + ": " + val("bericht")); }
    lines.push(""); lines.push(T.photos);
    return lines.join("\n");
  }
  function valid() {
    if (form.checkValidity()) return true;
    form.reportValidity();
    return false;
  }
  function track(kind) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: "offerte_" + kind });
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!valid()) return;
    track("whatsapp");
    window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(compose()), "_blank", "noopener");
  });
  var mailBtn = document.getElementById("quote-mail");
  if (mailBtn) {
    mailBtn.addEventListener("click", function (e) {
      e.preventDefault();
      if (!valid()) return;
      track("email");
      window.location.href = "mailto:" + MAIL + "?subject=" + encodeURIComponent(T.subject) + "&body=" + encodeURIComponent(compose());
    });
  }

})();
