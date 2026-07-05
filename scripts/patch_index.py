import sys
p = sys.argv[1]
src = open(p).read()
reps = [
("""      <p class="hint">We will announce you as a speaker across social media and event materials. Send us the portrait you want the region to see &#8212; <b>the highest quality you have</b> (a professional shoot or an original camera photo, not a screenshot).</p>
      <div class="drop" id="photoDrop">
        <div class="big">Upload your photo</div>
        <small>JPG / PNG / HEIC &#183; at least 1600px wide recommended &#183; up to 25 MB</small>
      </div>""",
"""      <p class="hint">We will announce you as a speaker across social media and event materials. Send us the portrait you want the region to see &#8212; <b>the best version you have</b>.</p>
      <div class="drop" id="photoDrop">
        <div class="big">Upload your photo</div>
        <small>Any photo works &#183; up to 30 MB</small>
      </div>"""),
("kind: 'photo', minSide: 1000", "kind: 'photo', minSide: 0"),
("""    if (file.size > 25 * 1024 * 1024) {
      msg.textContent = 'That file is over 25 MB. Please send a version under 25 MB.';""",
"""    if (file.size > 30 * 1024 * 1024) {
      msg.textContent = 'That file is over 30 MB. Please send a version under 30 MB.';"""),
("""    if (k === 'photo' && file.type.indexOf('image/') === 0 && window.createImageBitmap) {
      createImageBitmap(file).then(function (bm) {
        var short = Math.min(bm.width, bm.height);
        if (short < u.minSide) {
          msg.textContent = 'This photo is ' + bm.width + 'x' + bm.height + ' - too small for print and press. Please upload an original photo at least 1600px wide.';
          msg.style.display = 'block';
          $(u.drop).classList.add('err');
          return;
        }
        $(u.drop).classList.remove('err');
        if (short < 1600) toast('That works, though a larger original would print even better');
        makeThumb(file);
        proceed();
      }).catch(proceed);
    } else proceed();""",
"""    if (k === 'photo' && file.type.indexOf('image/') === 0 && window.createImageBitmap) {
      makeThumb(file);
    }
    proceed();"""),
("""    xhr.timeout = 180000;
    xhr.upload.onprogress = function (ev) {
      if (ev.lengthComputable) $(u.bar).style.width = Math.max(4, Math.round(100 * ev.loaded / ev.total)) + '%';
    };
    var finish = function (ok) {""",
"""    xhr.timeout = 180000;
    // Do NOT attach any listener to xhr.upload: doing so makes this a
    // non-simple CORS request, which triggers a preflight OPTIONS that Apps
    // Script cannot answer, silently blocking the whole upload. Instead show an
    // indeterminate bar that eases toward 90% while the POST is in flight.
    setTimeout(function () {
      $(u.bar).style.transition = 'width 10s ease-out';
      $(u.bar).style.width = '90%';
    }, 30);
    var finish = function (ok) {
      $(u.bar).style.transition = 'width .2s';"""),
("  var firstName = linkName.split(' ')[0] || 'Speaker';",
"  var firstName = linkName.trim() || 'Speaker';"),
("""    if (j.name) {
      firstName = j.name.split(' ')[0];
      $('r-name').textContent = firstName;
    }""",
"""    if (j.name) {
      firstName = String(j.name).trim();
      $('r-name').textContent = firstName;
    }"""),
]
n = 0
for old, new in reps:
    if old in src:
        src = src.replace(old, new, 1); n += 1
open(p, 'w').write(src)
print('applied', n, 'of', len(reps))
