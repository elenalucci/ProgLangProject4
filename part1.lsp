(defun demo()
	(setq fp(open "theString.txt" :direction :input))
	(setq fsaChar (read  fp "done"))
	(princ "processing")
	(princ fsaChar)
	(fsa fsaChar)
)

(defun fsa(fsaChar)
	(cond 
		((NULL fsaChar) (pprint "illegal empty fsa string"))
		(t(state0 fsaChar))
	)
)

(defun state0(fsaChar)
	(cond
		((EQ 'x (car fsaChar))(state0(cdr fsaChar)))
		((EQ 'y (car fsaChar))(state1(cdr fsaChar)))
		((NULL fsaChar) (pprint "illegal fsa string: state 0 is not an accept state"))
		(t (pprint "illegal character in state 0"))
	)
)

(defun state1(fsaChar)
	(cond
		((EQ 'x (car fsaChar))(state2(cdr fsaChar)))
		((NULL fsaChar) (pprint "legal fsa string"))
		(t (pprint "illegal character in state 1"))
	)
)

(defun state2(fsaChar)
	(cond
		((EQ 'x (car fsaChar))(state2(cdr fsaChar)))
		((EQ 'y (car fsaChar))(state3(cdr fsaChar)))
		((NULL fsaChar) (pprint "illegal fsa string: state 2 is not an accept state"))
		(t (pprint "illegal character in state 2"))
	)
)

(defun state3(fsaChar)
	(cond
		((EQ 'x (car fsaChar))(state3(cdr fsaChar)))
		((EQ 'z (car fsaChar))(state4(cdr fsaChar)))
		((NULL fsaChar)(pprint "legal fsa string"))
		(t (pprint "illegal character in state 3"))
	)
)

(defun state4(fsaChar)
	(cond
		((EQ 'x (car fsaChar))(state4(cdr fsaChar)))
		((EQ 'a (car fsaChar))(state1(cdr fsaChar)))
		((NULL fsaChar) (pprint "illegal fsa string: state 4 is not an accept state"))
		(t (pprint "illegal character in state 4"))
	)
)

