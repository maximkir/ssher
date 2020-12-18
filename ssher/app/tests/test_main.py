from ssher.app.main import connect

from click.testing import CliRunner


def test_connect(function_scoped_container_getter):
    container = function_scoped_container_getter.get("openssh-server")
    hostname = container.network_info[0].hostname
    port = container.network_info[0].host_port
    username = container.environment['USER_NAME']
    runner = CliRunner()
    result = runner.invoke(connect, [hostname, "-l", username, "-p", port])
    assert result.exit_code == 0

