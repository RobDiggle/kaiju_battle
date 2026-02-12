window.play_sound_effects = function(filename) {
  const a = new Audio("/static/sfx/" + filename);
  a.play();
};