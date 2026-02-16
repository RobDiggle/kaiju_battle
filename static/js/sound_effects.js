window.play_sound_effects = function(filename) {
  const a = new Audio("/static/sfx/" + filename);
  a.play();
};

// static/js/sound_effects.js

const SFX = {
  Megalon: {
    attack:  "/static/sfx/megalon_attack.mp3",
    defend:  "/static/sfx/megalon_defend.mp3",
    special: "/static/sfx/megalon_special.mp3",
  },
  Godzilla: {
    attack:  "static\sfx\godzilla_sound.mp3",
    defend:  "/static/sfx/godzilla_sound.mp3",
    special: "/static/sfx/godzilla_sound.mp3",
  },
  // add others
};

function play_sound_effects(btn) {
  const kaiju = btn.dataset.kaiju;
  const move  = btn.dataset.move;

  const src = SFX?.[kaiju]?.[move];
  if (!src) return;

  const audio = document.getElementById("sfx");
  if (!audio) return;

  audio.src = src;
  audio.currentTime = 0;
  audio.play();
}

window.play_sound_effects = play_sound_effects;
