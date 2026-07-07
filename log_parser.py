class LogParser:

    ERROR_KEYWORDS = [
        "ERROR",
        "Exception",
        "Traceback",
        "Failed",
        "CRITICAL"
    ]

    WARNING_KEYWORDS = [
        "WARNING",
        "WARN"
    ]

    TRACEBACK_KEYWORDS = [
        "Traceback"
    ]

    CRITICAL_KEYWORDS = [
        "ERROR",
        "CRITICAL",
        "FAILED",
        "EXCEPTION",
        "Connection refused",
        "Timeout",
        "Permission denied"
    ]

    def load_log(self, file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:
            lines = f.readlines()

        return [
            line.rstrip("\n")
            for line in lines
        ]


    def extract_errors(self, lines):

        return [
            line
            for line in lines
            if any(
                keyword in line
                for keyword in self.ERROR_KEYWORDS
            )
        ]


    def extract_warnings(self, lines):

        return [
            line
            for line in lines
            if any(
                keyword in line
                for keyword in self.WARNING_KEYWORDS
            )
        ]


    def extract_tracebacks(self, lines):

        return [
            line
            for line in lines
            if any(
                keyword in line
                for keyword in self.TRACEBACK_KEYWORDS
            )
        ]


    def extract_critical_events(self, lines):

        return [
            line
            for line in lines
            if any(
                keyword in line
                for keyword in self.CRITICAL_KEYWORDS
            )
        ]


    def summarize(self, lines):

        errors = self.extract_errors(lines)
        warnings = self.extract_warnings(lines)
        tracebacks = self.extract_tracebacks(lines)
        critical_events = self.extract_critical_events(lines)

        return {
            "total_lines": len(lines),
            "total_errors": len(errors),
            "total_warnings": len(warnings),

            "first_error": errors[0] if errors else "None",
            "last_error": errors[-1] if errors else "None",

            "detected_errors": errors[:10],
            "detected_warnings": warnings[:10],

            "tracebacks": tracebacks[:5],
            "critical_events": critical_events[:10]
        }