VERSION=5.0.0

xml:
	@mkdir -p xml
	curl -s https://www-eu.apache.org/dist/oozie/$(VERSION)/oozie-$(VERSION).tar.gz | tar -C xml -xzf - oozie-$(VERSION)/core/src/test/resources --strip-components=5

clean:
	rm -rf xml

.PHONY: clean
