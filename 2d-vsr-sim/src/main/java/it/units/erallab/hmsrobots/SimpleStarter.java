/*
 * Copyright (C) 2020 Eric Medvet <eric.medvet@gmail.com> (as alikhan4812)
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful, but
 *  WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package it.units.erallab.hmsrobots;

import com.google.common.collect.Lists;
import it.units.erallab.hmsrobots.core.controllers.TimeFunctions;
import it.units.erallab.hmsrobots.core.objects.ControllableVoxel;
import it.units.erallab.hmsrobots.core.objects.Robot;
import it.units.erallab.hmsrobots.tasks.Locomotion;
import it.units.erallab.hmsrobots.util.Grid;
import it.units.erallab.hmsrobots.viewers.GridEpisodeRunner;
import it.units.erallab.hmsrobots.viewers.GridOnlineViewer;
import org.apache.commons.lang3.tuple.Pair;
import org.dyn4j.dynamics.Settings;

import java.io.IOException;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;

public class SimpleStarter {
    public static void main(String[] args) throws IOException {
        final Grid<Boolean> structure = Grid.create(7, 4, (x, y) -> (x < 2) || (x >= 5) || (y > 0));
        Settings settings = new Settings();
        settings.setStepFrequency(1d / 30d);
        //int controlInterval = 1;          //main file also don't use it..used only to show what assumption was made
        //simple
        double f = 1d;
        Robot<ControllableVoxel> phasesRobot = new Robot<>(
                new TimeFunctions(Grid.create(
                        structure.getW(),
                        structure.getH(),
                        (final Integer x, final Integer y) -> (Double t) -> Math.sin(-2 * Math.PI * f * t + Math.PI * ((double) x / (double) structure.getW()))
                )),
                Grid.create(structure, b -> b ? new ControllableVoxel() : null)
        );


        List<Locomotion.Metric> metrics = Lists.newArrayList(Locomotion.Metric.CENTER_AVG_Y);
        metrics.add(Locomotion.Metric.TOTAL_Y_CHANGE);
        metrics.add(Locomotion.Metric.ABSOLUTE_Theta_CHANGE);
        //episode
        Locomotion locomotion = new Locomotion(
                60,
                Locomotion.createTerrain("uneven5"),
                metrics,
                settings
        );
        Grid<Pair<String, Robot>> namedSolutionGrid = Grid.create(1, 1);
        namedSolutionGrid.set(0, 0, Pair.of("phases", phasesRobot));

        ScheduledExecutorService uiExecutor = Executors.newScheduledThreadPool(4);
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        GridOnlineViewer gridOnlineViewer = new GridOnlineViewer(Grid.create(namedSolutionGrid, Pair::getLeft), uiExecutor);
        gridOnlineViewer.start(5);
        GridEpisodeRunner<Robot> runner = new GridEpisodeRunner<>(
                namedSolutionGrid,
                locomotion,
                gridOnlineViewer,
                executor
        );
        runner.run();
    }


}
