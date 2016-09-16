realtime:
	inotifywait -q -m -e close_write --format %e slides.md | \
	while read events; do \
  		make reveal; \
	done

reveal:
	pandoc -t revealjs \
	  --section-divs --standalone \
	  --variable theme="sky" \
	  --variable transition="linear" \
	  --variable section-titles="true" \
	  slides.md -o slides.html

pdf:
	pandoc -t beamer \
	--variable theme="AnnArbor" \
	--variable colortheme="beaver" \
	--variable fonttheme="structurebold" \
	slides.md -o slides.pdf

serve:
	python -m http.server

clean:
	rm slides.html
	rm slides.pdf