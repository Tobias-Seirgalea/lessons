from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

# Resources can be found at
    # https://resources.gem5.org/
# riscv-matrix-multiply is obtained from
    # https://resources.gem5.org/resources/riscv-getting-started-benchmark-suite?version=1.0.0

workload = obtain_resource("riscv-matrix-multiply-run")
board.set_workload(workload)

#Instantiate and set parameters
cache1 = PrivateL1SharedL2CacheHierarchy(
    lld_size = "16kB",
    lli_size = "16kB",
    l2_size  = "256kB",
    lld_assoc = 8,
    lli_assoc = 8,
    l2_assoc = 16
)

#plg into board
board = x86Board(
    cache_hierarchy = cache1,
)

board.set_workload(workload)
simulator = Simulator(board=board)
simulator.run()

cache2 = PrivateL1PrivateL2CacheHierarchy(
    lld_size = "16kB",
    lli_size = "16kB",
    l2_size  = "32kB",
    lld_assoc = 8,
    lli_assoc = 8,
    l2_assoc = 8
)

board.set_workload(workload)
simulator = Simulator(board=board)
simulator.run()
