from log_inspector.analyzer import analyze_lines

def test_analyze_lines():
    sample_logs = [
        'Kernel: error occurred during operation',
        'systemd: warning: low memory',
        'network: fail to connect',
        'normal info message',
    ]

    result = analyze_lines(sample_logs)

    assert result['error'] == 1
    assert result['warn'] == 1
    assert result['fail'] == 1
    