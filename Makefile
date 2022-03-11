IN=tests/in/$(CTG)/test$(TEST).in
OUT=tests/out/$(CTG)/test$(TEST).out
AUX=tests/aux/$(CTG)/test$(TEST).aux

build:
	#complete if necessary

run_backtracking:
	python3.9 kCliqueBKT.py $(IN) > $(OUT)

run_reduction:
	python3.9 kCliqueReduction.py $(IN) > $(AUX)

clean:
	#complete if necessary
