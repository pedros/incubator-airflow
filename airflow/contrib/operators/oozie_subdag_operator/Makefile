VERSION=5.0.0

xsd:
	@mkdir -p xsd
	curl -s https://www-eu.apache.org/dist/oozie/$(VERSION)/oozie-$(VERSION).tar.gz | tar -C xsd -xzf - oozie-$(VERSION)/client/src/main/resources --strip-components=5

clean:
	rm -rf xsd

.PHONY: clean
