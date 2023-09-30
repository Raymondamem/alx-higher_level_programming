#include <Python.h>

void print_python_string(PyObject *p) {
	if (!PyUnicode_Check(p)) {
		printf("[ERROR] Invalid String Object\n");
		return;
	}

	Py_ssize_t size = PyUnicode_GET_SIZE(p);
	char *value = PyUnicode_AsUTF8(p);

	printf("[.] string object info\n");
	printf("  type: %s\n", PyUnicode_IS_COMPACT(p) ? "compact" : "non-compact");
	printf("  length: %zd\n", size);
	printf("  value: %s\n", value);
}
